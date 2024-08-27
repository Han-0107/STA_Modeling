class CellData():
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        vector = self.data[index]
        labels = vector[:2]
        inputs = vector[2:]
        return inputs, labels
    
    def __len__(self):
        return len(self.data)