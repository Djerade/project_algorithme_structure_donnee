class Stack:
    def  __init__(self) -> None:
        self.items = []
        
    def stack_empty(self):
        return len(self.items) == 0
    
    def add_task(self, item):
        return self.items.append(item)
    
    def delete_task(self):
        if not self.stack_empty():
            self.items.pop()
        else:
            print('our stack  is empty')
    
    def get_task(self):
        if not self.stack_empty():
            return self.items[-1]
        else:
            print('our stack  is empty')
    
    def size_stack(self):
        return len(self.items)