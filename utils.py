def read_file():
    filename = input("Enter filename:")
    if not filename.strip():
        raise BadRequest("Cannot be blank.")
    file = open(filename)
    return file


def test_valid_file_name_and_extension(filename, extension):
    if filename.split(".")[1:] in [[
            extension
    ]] and filename[0].isalpha() and sum(c.isdigit() for c in filename) < 4:
        return True
    else:
        raise BadRequest("Invalid File")
