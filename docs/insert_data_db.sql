DELETE FROM backend_enumfieldtypesmodel WHERE id>0;
DELETE FROM backend_fieldtypesmodel WHERE id>0;
DELETE FROM backend_risktypesmodel WHERE id>0;

INSERT INTO  backend_risktypesmodel (id, risk_type_name) 
VALUES (1, 'Property-based'), 
	   (2, 'Automobile Policies'), 
	   (3, 'Cyber Liability Coverage'),
	   (4, 'Prize Insurance');

INSERT INTO backend_fieldtypesmodel (id, risktype_id, field_name, field_type) 
VALUES (1, 1, 'Address', 'text'), 
	   (2, 2, 'Model', 'text'), 
	   (3, 3, 'Serial Number', 'text'),
	   (4, 3, 'Begin Date', 'date'),
	   (5, 4, 'Maximum Prize', 'number'),	   	   
	   (6, 4, 'Area Coverage', 'enum'),
	   (7, 2, 'Coverage levels', 'enum'),
		(8, 2, 'Number of Passengers', 'number');	   


INSERT INTO backend_enumfieldtypesmodel (fieldtypes_id, enum_value) 
VALUES (6, 'NY'), 
	   (6, 'MI'),
	   (6, 'AL'),
	   (6, 'AK'),
	   (6, 'AR'),
	   (6, 'KS'),
	   (6, 'LA'),
	   (7, 'The insured party (medical payments)'),
	   (7, 'Property damage caused by the insured'),
	   (7, 'The insured vehicle (physical damage)'),
	   (7, 'Third parties (car and people, property damage and bodily injury)'),
	   (7, 'Third party, fire and theft'),
	   (7, 'In some jurisdictions coverage for injuries to persons riding in the insured vehicle is available without regard to fault in the auto accident (No Fault Auto Insurance)'),
	   (7, 'The cost to rent a vehicle if yours is damaged.'),
	   (7, 'The cost to tow your vehicle to a repair facility.'),
	   (7, 'Accidents involving uninsured motorists.');



