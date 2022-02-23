# -*-coding:utf-8-*-
import openpyxl
import pytest


def get_excel():
    # 解析excel数据
    # return [[1, 1, 2],[3,6,9],[7,8,15]]

    # 1,读取工作簿
    book = openpyxl.load_workbook('./params.xlsx')
    # 2,读取工作表
    sheet = book.active
    # 3,读取单元格
    cell_a1 = sheet['A1']
    # A3
    # cell_a3 = sheet.cell(column=1, row=3)
    # print(cell_a3.value)
    # 读取多个连续单元格
    cells = sheet["A1":"C3"]
    print(cells)
    # 获取单元格的值
    values = []
    for row in cells:
        data = []
        for cell in row:
            data.append(cell.value)
        values.append(data)
    print(values)
    return values
def my_add(x, y):
    return x+y

class TestWithEXCEL:
    @pytest.mark.parametrize('x,y,expected', get_excel())
    def test_add(self,x,y,expected):
        assert my_add(int(x), int(y)) == int(expected)
