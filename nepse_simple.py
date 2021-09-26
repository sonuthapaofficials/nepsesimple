# /bin/env python

# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k8T91ug1-HAPxvYj9d88EUTIguMZ3QwO
"""

import requests
import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

url = "https://www.nepalipaisa.com/Market-Mover.aspx"
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]

df1 = df.sort_values(by=["Closing Price"])
df1.pop("Symbols")

slice_ = ["% Change"]


def highlight_max(s, props=""):
    return np.where(s <= 0, props, "")


df2 = df1.style.apply(
    highlight_max, props="color:red;", axis=0, subset=slice_
).set_properties(subset=slice_)


loc = "nepse_simple.xlsx"

df1.to_csv("mydata.csv")

df1.to_html("index.html")

df2.to_excel(loc)

oxl = openpyxl.load_workbook(loc)
oxl.sheetnames

sheet = oxl.active

ws = sheet
dims = {}
for row in ws.rows:
    for cell in row:
        if cell.value:
            dims[cell.column_letter] = max(
                (dims.get(cell.column_letter, 0), len(str(cell.value)))
            )
for col, value in dims.items():
    ws.column_dimensions[col].width = value


oxl.save(loc)


url2 = 'http://www.nepalstock.com/indices'
html2 = requests.get(url).content
df_list2 = pd.read_html(html2)
df22 = df_list2[-1]

data2=np.array(df22)
data2=np.flip(data2)
plot=data2[1:data2.shape[0],2]

plt.figure(figsize=(40, 25))
plt.plot(plot,'go--')
plt.savefig('graph.png')
