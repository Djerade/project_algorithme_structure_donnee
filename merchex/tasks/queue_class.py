from datetime import datetime

class Queues:
    def __init__(self) -> None:
        self.items = []
        
    def stack_empty(self):
        return len(self.items) == 0
    
    def add_task(self, item):
        return self.items.append(item)
    
    def delete_task(self):
        if not self.stack_empty():
            self.items.pop(0)
        else:
            print('our queue  is empty')
    
    def get_task(self):
        if not self.stack_empty():
            return self.items[0]
        else:
            print('our queue  is empty')
            
    def size_queue(self):
        return len(self.items)
    
    def get_all(self):
        return self.items