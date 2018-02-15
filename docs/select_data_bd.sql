select rt.*, ft.*, fe.*
from backend_risktypesmodel as rt
full join backend_fieldtypesmodel as ft
on rt.id=ft.risktype_id
left join backend_enumfieldtypesmodel as fe
on ft.id=fe.fieldtypes_id;



