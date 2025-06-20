expression_value = list(map(float, input("Enter the gene expression data values: ").split(",")))
data = []
for value in expression_value:
    if value < 5:
        data.append("underexpressed")
    elif 5 <= value <= 15:
        data.append("normal")
    else:
        data.append("overexpressed")

print(data)
