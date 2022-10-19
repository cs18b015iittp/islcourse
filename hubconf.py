def load_data():

 
    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=False,
        transform=ToTensor(),
    )

   
    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=False,
     
        transform=ToTensor(),
    )
    
    return training_data, test_data
   
class ModifiedDataset(Dataset):
  def __init__(self,given_dataset,shrink_percent=10):
    self.given_dataset = given_dataset
    self.shrink_percent = shrink_percent
    
    
  def __len__(self):
    return len(self.given_dataset)

  def __getitem__(self,idx):
    img, lab = self.given_dataset[idx]
