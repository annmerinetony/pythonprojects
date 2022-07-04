bills = [
    {"billno": 1000, "total": 1200, "items":
        [
            {"item_name": "bread", "qty": 2, "mrp": 35},
            {"item_name": "milk", "qty": 2, "mrp": 25},
            {"item_name": "jam", "qty": 2, "mrp": 70},
            {"item_name": "egg", "qty": 50, "mrp": 250},
            {"item_name": "horlicks", "qty": 1, "mrp": 250},

        ]},
    {"billno": 1001, "total": 1300, "items":
        [
            {"item_name": "nanpro", "qty": 1, "mrp": 670},
            {"item_name": "sugar", "qty": 5, "mrp": 40},
            {"item_name": "oreo", "qty": 4, "mrp": 40},
            {"item_name": "wheat", "qty": 5, "mrp": 50},
            {"item_name": "horlicks", "qty": 1, "mrp": 250},

        ]},
    {"billno": 1003, "total": 1000, "items":
        [
            {"item_name": "nanpro", "qty": 1, "mrp": 670},
            {"item_name": "sugar", "qty": 5, "mrp": 40},
            {"item_name": "oreo", "qty": 4, "mrp": 40},
            {"item_name": "wheat", "qty": 5, "mrp": 50},
            {"item_name": "horlicks", "qty": 1, "mrp": 250},

        ]},
    {"billno": 1004, "total": 300, "items":
        [

            {"item_name": "wheat", "qty": 5, "mrp": 50},
            {"item_name": "horlicks", "qty": 1, "mrp": 250},

        ]
     },
    {"billno": 1005, "total": 1300, "items":
        [
            {"item_name": "nanpro", "qty": 1, "mrp": 670},
            {"item_name": "sugar", "qty": 5, "mrp": 40},
            {"item_name": "oreo", "qty": 4, "mrp": 40},
            {"item_name": "wheat", "qty": 5, "mrp": 50},
            {"item_name": "horlicks", "qty": 1, "mrp": 250},

        ]},

]

gt_amt=[bill for bill in bills if bill["total"]>1200]
print(gt_amt)
gt_amt=list(filter(lambda bill:bill["total"]>1200,bills))
print(gt_amt)
total=sum(list(map(lambda bill:bill["total"],bills)))
print(total)
val_cust=max(bills,key=lambda bill:bill["total"])
print(val_cust)
qty_horlicks=sum([item["qty"] for bill in bills for item in bill["items"] if item["item_name"]=="horlicks"])
print(qty_horlicks)
qty_horlicks=sum([item["qty"] for bill in bills for item in bill["items"] if item["item_name"]=="sugar"])
print(qty_horlicks)