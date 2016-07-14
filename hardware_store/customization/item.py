import frappe

@frappe.whitelist()
def get_item_uom(item_code):
	stock_uom = frappe.db.get_value("Item", item_code, "stock_uom")
	if not item_code:
		frappe.throw("please select the item")
	else:
		uoms = frappe.db.get_values("UOM Conversion Detail", 
				{ "parent":item_code, "uom": ["!=", stock_uom]}, "uom")
		if not uoms:
			return stock_uom
		else:
			uoms = [uom[0] for uom in uoms]
			uoms.insert(0, stock_uom)
			return ",".join(uoms)