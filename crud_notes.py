import os
import csv
class notes_worker():
    def __init__(self):
        self.file = "notes.csv"
        if not os.path.exists(self.file):
            with open(self.file, "w") as notes:
                self.writer = csv.DictWriter(notes, fieldnames=["ID", "Note"])
                self.writer.writeheader()
                self.num_note = 1
        else:
            with open(self.file, "r") as notes:
                reader = csv.DictReader(notes)
                for i in reader:
                    self.num_note = int(i["ID"]) + 1

    def readAll(self):
        with open(self.file) as notes:
            file_reader = csv.DictReader(notes)
            for i in file_reader:
                print(f"{i['ID']}: {i['Note']}")

    def readNote(self, num_note: int):
        with open(self.file) as notes:
            file_reader = csv.DictReader(notes)
            for i in file_reader:
                if int(i["ID"]) == num_note:
                    print(i)
                    return
        print("This note not found")

    def updateNote(self, num_note:int, new_data:str):
        with open(self.file, "r") as notes:
            reader = csv.DictReader(notes)
            tmp_data = []
            found = False
            for i in reader:
                tmp_data.append(i)
                if int(i["ID"]) == num_note:
                    found = True
            if not found:
                print("This note not found!")
                return
        with open(self.file, "w") as notes:
            writer = csv.DictWriter(notes, fieldnames=["ID", "Note"])
            writer.writeheader()

            for i in tmp_data:
                if int(i["ID"]) == num_note:
                    writer.writerow({"ID": num_note, "Note": new_data})
                    continue
                writer.writerow({"ID": i["ID"], "Note": i["Note"]})

    def addNote(self, note: str):
        with open(self.file, "a") as notes:
            self.writer = csv.DictWriter(notes, fieldnames=["ID", "Note"])
            self.writer.writerow({"ID": self.num_note,
                                  "Note":note})
            self.num_note += 1

    def deleteNote(self, num_note: int):
        with open(self.file, "r") as notes:
            reader = csv.DictReader(notes)
            tmp_data = []
            found = False
            for i in reader:
                if int(i["ID"]) == num_note:
                    found = True
                    continue
                tmp_data.append(i)
            if not found:
                print("This note not found!")
                return
        with open(self.file, "w") as notes:
            writer = csv.DictWriter(notes, fieldnames=["ID", "Note"])
            writer.writeheader()

            counter = 1
            for i in tmp_data:
                writer.writerow({"ID": counter, "Note": i["Note"]})
                counter += 1
            self.num_note = counter + 1

if __name__ == "__main__":
    test = notes_worker()
    #test.addNote("test2")
    test.readAll()
    #test.updateNote(3, "testtest")
    test.deleteNote(4)
    print("---------------------------------")
    test.readAll()