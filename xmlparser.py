import xml.etree.ElementTree as ET
import os


def xmlParse(dir):
    tree = ET.parse(dir)
    root = tree.getroot()
    package_list = []
    className = ""
    super_class_list = []
    super_interface_list = []
    field_list = []
    method_list = []
    # 遍历xml文档的第二层
    for child in root:
        if child.tag == "Id":
            pass
        elif child.tag == "Package":
            if child.text != "":
                package_list.append(child.text)
        elif child.tag == "ClassName":
            if child.text != "":
                className = child.text
        elif child.tag == "SuperClass":
            if child.text != "":
                super_class_list.append(child.text)
        elif child.tag == "SuperInterfaceList":
            if child.text != "":
                super_interface_list.append(child[0].text)
        elif child.tag == "FieldList":
            for children in child:
                # Field
                if children.tag == "Field":
                    temp_field = [0, 0]
                    for childrenen in children:
                        if childrenen.tag == "FieldName":
                            temp_field[0] = childrenen.text
                        if childrenen.tag == "FieldType":
                            temp_field[1] = childrenen.text
                    field_list.append(tuple(temp_field))
        elif child.tag == "MethodList":
            for children in child:
                # Method
                if children.tag == "Method":
                    temp_method = [0, 0, [], []]
                    for childrenen in children:
                        if childrenen.tag == "MethodName":
                            temp_method[0] = childrenen.text
                        elif childrenen.tag == "ReturnType":
                            temp_method[1] = childrenen.text
                        elif childrenen.tag == "ParameterList":
                            for childrenenen in childrenen:
                                if childrenenen.tag == "ParameterType":
                                    temp_method[2].append(childrenenen.text)
                        elif childrenen.tag == "ThrowExceptionList":
                            for childrenenen in childrenen:
                                if childrenenen.tag == "ExceptionType":
                                    temp_method[3].append(childrenenen.text)
                    method_list.append(tuple(temp_method))
    return (className, package_list, super_class_list, super_interface_list, field_list, method_list)

def xmlParseToTriple(file_name,xmlParseResult):
    (className,package_list,super_class_list,super_interface_list,field_list,method_list) = xmlParseResult
    file_name = file_name.replace(".xml","")
    if file_name != className:
        print(file_name)
    with open("./data/eTour/eTour_ea2class.txt","a",encoding="utf-8",newline="") as file :
        file.write(file_name+"\t"+className+"\t"+"class"+"\n")
        for field in field_list:
            file.write(file_name+"\t"+field[0]+"\t"+"field"+"\n")
        for method in method_list:
            file.write(file_name+"\t"+method[0]+"\t"+"method"+"\n")
    with open("./data/eTour/eTour_xmlParseResult.txt","a",encoding="utf-8") as file :
        for package in package_list:
            if package is not None:
                file.write(package+"\t"+className+"\tcontain"+"\n")
        for super_class in super_class_list:
            if super_class is not None:
                file.write(className+"\t"+super_class+"\tsuper_class"+"\n")
        for super_interface in super_interface_list:
            if super_interface is not None and super_interface.replace("\n","").strip() is not "":
                file.write(className+"\t"+super_interface+"\tsuper_interface"+"\n")
        for field in field_list:
            if field[0] is not None:
                file.write(className+"\t"+field[0]+"\tfield"+"\n")
            if field[1] is not None:
                file.write(field[0]+"\t"+field[1]+"\tfield_type"+"\n")
        for method in method_list:
            if method[0] is not None:
                file.write(className+"\t"+method[0]+"\tmethod"+"\n")
            if method[1] is not None:
                file.write(method[0]+"\t"+method[1]+"\treturn_type\n")
            for para in method[2]:
                if para is not None:
                    file.write((method[0]+"\t"+para+"\tparameter\n"))
            for exception in method[3]:
                if exception is not None:
                    file.write((method[0]+"\t"+exception+"\tthrow_exception\n"))



def file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root, end=' ')  # 当前目录路径
        # print(dirs, end=' ')    # 当前路径下的所有子目录
        # print(files)            # 当前目录下的所有非目录子文件
        print(os.walk(file_dir))
        return root, dirs, files


if __name__ == '__main__':
    root, dirs, files = file_path("./data/eTour/eTour_xml/")
    for file in files:
        xmlParseToTriple(file,xmlParse(root+file))
