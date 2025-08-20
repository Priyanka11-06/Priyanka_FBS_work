Dict = {"Name":"Priya","Age":21,"city":"pune"}

To_remove = "Age"
if To_remove in Dict:
    del Dict[To_remove]

print("Dictionary after remove",Dict)