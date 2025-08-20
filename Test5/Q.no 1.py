D = [2000, 500, 200, 100, 50, 20, 10, 5]

def min_notes(amt):
    notes_used = {}
    for note in D:
        if(amt >= note):
            count = amt // note
            notes_used[note] = count 
            amt = amt % note
    return notes_used 

amt = 4855
result = min_notes(amt)
print("notes used", result)
print("minimun number of notes", sum(result.values()))
