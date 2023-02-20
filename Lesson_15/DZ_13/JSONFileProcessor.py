class JSONFileProcessor(FileProcessor):
    """
    Class to represent a JSON file processor.
    """

    def read_file(self):
        """
        Reads data from a JSON file and appends it to data_entries list.
        """
        with open(self.filename) as f:
            json_data = json.load(f)
            for data in json_data:
                self.data_entries.append(DataEntry(data))
