from typing import List

from unicodedata import category

from project_03.category import Category
from project_03.document import Document
from project_03.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        searched_category = [cat for cat in self.categories if cat.id == category_id][0]
        searched_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        searched_topic = [top for top in self.topics if top.id == topic_id][0]
        searched_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        searched_document = [doc for doc in self.documents if doc.id == document_id][0]
        searched_document.edit(new_file_name)

    def delete_category(self, category_id):
        searched_category = [cat for cat in self.categories if cat.id == category_id][0]
        self.categories.remove(searched_category)

    def delete_topic(self, topic_id):
        searched_topic = [top for top in self.topics if top.id == topic_id][0]
        self.topics.remove(searched_topic)

    def delete_document(self, document_id):
        searched_document = [doc for doc in self.documents if doc.id == document_id][0]
        self.documents.remove(searched_document)

    def get_document(self, document_id):
        searched_document = [doc for doc in self.documents if doc.id == document_id][0]
        return searched_document.__repr__()

    def __repr__(self):
        return '\n'.join([doc.__repr__() for doc in self.documents])


#
# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project_03")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
