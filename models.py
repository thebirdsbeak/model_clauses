from docxtpl import DocxTemplate
from datetime import datetime

variable_list = {"entry_date": "",
                 "export_name": "",
                 "export_address": "",
                 "export_tel": "",
                 "export_fax": "",
                 "export_email": "",
                 "export_other": "",
                 "export_jurisdiction": "",
                 "export_signer_name": "",
                 "export_signer_pos": "",
                 "export_signer_address": "",
                 "import_name": "",
                 "import_address": "",
                 "import_tel": "",
                 "import_fax": "",
                 "import_email": "",
                 "import_other": "",
                 "import_signer_name": "",
                 "import_signer_pos": "",
                 "import_signer_address": "",
                 "export_activities": "",
                 "import_activities": "",
                 "data_subjects": "",
                 "data_categories": "",
                 "special_categories": "",
                 "processing_operations": "",
                 "technical_measures": ""}

print("Enter values or leave blank for defaults\n")

variable_list["entry_date"] = (datetime.now()).strftime("%d %B %Y")
export_name = input("Exporter name: ")
if not export_name:
    variable_list["export_name"] = "Please complete"
else:
    variable_list["export_name"] = export_name

export_address = input("Exporter address: ")
if not export_address:
    variable_list["export_address"] = "Please complete"
else:
    variable_list["export_address"] = export_address
export_tel = input("Exporter Tel: ")
variable_list["export_tel"] = export_tel
export_fax = input("Exporter Fax: ")
variable_list["export_fax"] = export_fax
export_email = input("Exporter Email: ")
if not export_email:
    variable_list["export_email"] = "Please complete"
else:
    variable_list["export_email"] = export_email
export_other = input("Exporter Other ID: ")
variable_list["export_other"] = export_other
export_jurisdiction = input("Exporter Seat: ")
if not export_jurisdiction:
    variable_list["export_jurisdiction"] = "Please complete"
else:
    variable_list["export_jurisdiction"] = export_jurisdiction
export_signer_name = input("Exporter Signer Name: ")
variable_list["export_signer_name"] = export_signer_name
export_signer_pos = input("Exporter Signer Position: ")
variable_list["export_signer_pos"] = export_signer_pos
export_signer_address = input("Exporter Signer Address: ")
variable_list["export_signer_address"] = export_signer_address

import_name = input("Importer Name: ")
if not import_name:
    variable_list["import_name"] = "Please complete"
else:
    variable_list["import_name"] = import_name

import_address = input("Importer Address: ")
if not import_address:
    variable_list["import_address"] = "Please complete"
else:
    variable_list["import_address"] = import_address
import_tel = input("Importer Tel: ")
variable_list["import_tel"] = import_tel
import_fax = input("Importer Fax: ")
variable_list["import_fax"] = import_fax
import_email = input("Importer Email: ")
if not import_email:
    variable_list["import_email"] = "Please complete"
else:
    variable_list["import_email"] = import_email
import_other = input("Importer Other ID: ")
variable_list["import_other"] = import_other
import_signer_name = input("Importer Signer Name: ")
variable_list["import_signer_name"] = import_signer_name
import_signer_pos = input("importer Signer Position: ")
variable_list["import_signer_pos"] = import_signer_pos
import_signer_address = input("Importer Signer Address: ")
variable_list["import_signer_address"] = import_signer_address

export_activities = input("Exporter activities: ")
if not export_activities:
    variable_list["export_activities"] = "Please complete"
else:
    variable_list["export_activities"] = export_activities
import_activities = input("Importer Activities: ")
if not import_activities:
    variable_list["import_activities"] = "Please complete"
else:
    variable_list["import_activities"] = import_activities
data_subjects = input("Data Subjects: ")
if not data_subjects:
    variable_list["data_subjects"] = "Please complete"
else:
    variable_list["data_subjects"] = data_subjects
data_categories = input("Data Categories: ")
if not data_categories:
    variable_list["data_categories"] = "Please complete"
else:
    variable_list["data_categories"] = data_categories
special_categories = input("Special Categories: ")
variable_list["special_categories"] = special_categories
processing_operations = input("Processing Operations: ")
if not processing_operations:
    variable_list["processing_operations"] = "Please complete"
else:
    variable_list["processing_operations"] = processing_operations
technical_measures = input("Technical Measures: ")
if not technical_measures:
    variable_list["technical_measures"] = "Please complete"
else:
    variable_list["technical_measures"] = technical_measures

doc = DocxTemplate("ctop.docx")

doc.render(variable_list)

import_name = import_name.replace(" ", "_")
export_name = export_name.replace(" ", "_")

file_name = "{}-{}-clauses.docx".format(import_name, export_name)

doc.save(file_name)
