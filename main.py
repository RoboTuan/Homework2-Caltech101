from caltech_dataset import Caltech

def main():
   train = Caltech("101_ObjectCategories", split='train')
   print(f"Length of the dataset {train.__len__}")
   print(train.__getitem__(5000))

   l = list(train.labels.values())
   l = sorted(l)
   print(l)


if __name__ == "__main__":
    main()