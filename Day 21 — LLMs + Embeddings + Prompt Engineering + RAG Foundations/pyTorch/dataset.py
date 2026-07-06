from torch.utils.data import Dataset
class StudentDataset(Dataset):

    def __len__(self):
        return len(data)

    def __getitem__(self,index):
        return data[index]