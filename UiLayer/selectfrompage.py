class SelectFromPage:
    def __init__(self,items: list):
        self.items=items
        self.endpage=5
        self.startpage=0
        pass
    
    def currentPage(self):
        items_list: list=self.items[self.startpage:self.endpage]
        page = []
        for num in range(len(items_list)):
            page.append(f'{num+1}. {items_list[num]}')
        page=('\n').join(page)
        return page
    
    def next_page(self):
        self.startpage+=5
        self.endpage+=5

        if self.startpage >= len(self.items):
            self.startpage = 0
            self.endpage = 5

    def select_item_by_number(self, number: int) -> str | None:
        item_list: list = self.items[self.startpage:self.endpage]
        if 1 <= number <= len(item_list):
            return item_list[number - 1]
        return None