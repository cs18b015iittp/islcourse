class LandmarkDataset(Dataset): 
     def __init__(self, image_paths, transform=False):
       self.image_paths = image_paths
         self.transform = transform
        
     def __len__(self):
         return len(self.image_paths)

    def __getitem__(self, idx): 
        image_filepath = self.image_paths[idx] 
        image = cv2.imread(image_filepath) 
         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
         label = image_filepath.split('/')[-2]
         label = class_to_idx[label]
         if self.transform is not None:
             image = self.transform(image=image)["image"]
        
        return image, label 
  
  
  
 train_dataset = LandmarkDataset(train_image_paths,train_transforms)
   valid_dataset = LandmarkDataset(valid_image_paths,test_transforms) 
  test_dataset = LandmarkDataset(test_image_paths,test_transforms)






 import matplotlib.pyplot as plt
 %matplotlib inline


def visualize_augmentations(dataset, idx=0, samples=10, cols=5, random_img = False):
    
     dataset = copy.deepcopy(dataset)
   
     dataset.transform = A.Compose([t for t in dataset.transform if not isinstance(t, (A.Normalize, ToTensorV2))])
     rows = samples // cols
    
        
     figure, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(12, 8))
   for i in range(samples):
         if random_img:
             idx = np.random.randint(1,len(train_image_paths))
       image, lab = dataset[idx]
         ax.ravel()[i].imshow(image)
       ax.ravel()[i].set_axis_off()
         ax.ravel()[i].set_title(idx_to_class[lab])
   plt.tight_layout(pad=1)
     plt.show()    

 visualize_augmentations(train_dataset,np.random.randint(1,len(train_image_paths)), random_img = True)



