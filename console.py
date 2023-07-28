def userTalk(num_command: str, notes_worker) -> None:

    match num_command:
        # read all
        case "1":
            notes_worker.readAll()
        # read one note
        case "2":
            notes_worker.readNote(int(input("Select note for read: ")))
        # write row
        case "3":
            notes_worker.addNote(input("Write your note: "))
        # update note
        case "4":
            num_note = int(input("Select updatable note: "))
            new_note = input("Write new data for note: ")
            notes_worker.updateNote(num_note, new_note)
        # delete note
        case "5":
            notes_worker.deleteNote(int(input("Select node for delete: ")))
