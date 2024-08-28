class CellData():
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        vector = self.data[index]
        labels = vector[6:]
        inputs = vector[:6]
        return inputs, labels
    
    def __len__(self):
        return len(self.data)