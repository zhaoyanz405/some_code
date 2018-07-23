### use find()

```python
role_list = await Role.find({'permission_code_list': {'$in': [PERMISSION_TYPE_ACTIVITY_MANAGEMENT]}}).to_list(5)

(Pdb) role_list
[<db.models.Role object at 0x7f4e6d60ba90>]
(Pdb) x=role_list[0]
(Pdb) x
<db.models.Role object at 0x7f4e6d60ba90>
(Pdb) x.code
'role1'
(Pdb) q

```

