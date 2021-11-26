import datetime
from xlsxwriter.workbook import Workbook
from django.core.exceptions import ObjectDoesNotExist
from django.forms.utils import pretty_name
import io


def multi_getattr(obj, attr, default=None):
    attributes = attr.split(".")

    for i in attributes:
        try:
            if obj._meta.get_field(i).choices:
                obj = getattr(obj, f"get_{i}_display")()
            else:
                obj = getattr(obj, i)
        except AttributeError:
            if default:
                return default
            else:
                raise

    return obj


def get_column_head(obj, name):
    names = name.split(".")

    tmp = ''

    for i in names:
        tmp += obj._meta.get_field(i).verbose_name
        tmp += '.'


    return pretty_name(tmp)


def get_column_cell(obj, name):
    try:
        attr = multi_getattr(obj, name)
    except ObjectDoesNotExist:
        return None

    if hasattr(attr, '_meta'):
        return str(attr).strip()
    elif hasattr(attr, 'all'):
        return ', '.join(str(x).strip() for x in attr.all())

    if isinstance(attr, datetime.datetime):
        from django.utils.timezone import localtime
        attr = localtime(attr)
        attr = attr.replace(tzinfo=None)

    return attr


def queryset_to_workbook(queryset,
                         columns):

    output = io.BytesIO()
    workbook = Workbook(output)
    
    header_style = workbook.add_format({'bold':True})
    default_style = workbook.add_format()
    cell_style_map = (
    (datetime.datetime, workbook.add_format({'num_format':"YYYY/MM/DD HH:MM"})),
    (datetime.date, workbook.add_format({'num_format':'DD/MM/YYYY'})),
    (datetime.time, workbook.add_format({'num_format':"HH:MM"})),
    (bool, workbook.add_format({'num_format':"BOOLEAN"})),
    )
    
    report_date = datetime.date.today()
    sheet_name = f"Export {report_date.strftime('%Y-%m-%d')}"
    sheet = workbook.add_worksheet(sheet_name)

    obj = queryset.first()
    

    for num, column in enumerate(columns):
        value = get_column_head(obj, column)
        sheet.write(0, num, value, header_style)

    for x, obj in enumerate(queryset, start=1):
        for y, column in enumerate(columns):
            value = get_column_cell(obj, column)
            style = default_style

            for value_type, cell_style in cell_style_map:
                if isinstance(value, value_type):
                    style = cell_style

                    break
            sheet.write(x, y, value, style)
    workbook.close()
    output.seek(0)
    
    return output
