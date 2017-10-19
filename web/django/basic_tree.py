"""
An abstract model to allow the creation of very simple relationship trees.
TODO: This can easily be improved upon. e.g. Not sure why I used so many lists...
"""

from django.db import models


class ParentAbstract(models.Model):
    """Abstract class to allow building hierarchical relationships"""
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                help_text='Self referential foreign key to relate an object with its parent')

    def get_root(self):
        """
        Recurse through the tree to get the first ancestor of an object
        :returns: The top level ancestor object
        """
        if self.parent is None:
            # Base case
            return self
        return self.parent.get_root()

    def get_children(self):
        """
        Using the 'type' of self, get the model to be used for the query.
        :returns: A list of child objects
        """
        model = type(self)
        children = model.objects.filter(parent=self)
        return [child for child in children]

    def get_ancestors(self, ancestors=None):
        """
        Recursively traverse the tree to get all ancestors
        :returns: A list of ancestors
        """
        if not ancestors:
            ancestors = []
        if not self.parent:
            # Base case
            return ancestors
        ancestors.append(self.parent)
        return self.parent.get_ancestors(ancestors)

    def get_all_children(self):
        """
        Traverse the tree to collect all direct children and decsendents
        :returns: A dictionary with the parent id as key, and a list of child ids as value
        """
        to_visit_children = [self]
        visited_children = set()
        all_children = dict()
        while to_visit_children:
            child = to_visit_children.pop()
            if child.parent_id in all_children:
                all_children[child.parent_id].append(child)
            all_children[child.pk] = []
            visited_children.add(child)
            to_visit_children.extend([kid for kid in child.get_children() if kid not in visited_children])
        return all_children

    def get_siblings(self):
        """
        Using the 'type' of self, get the model to be used for the query.
        :returns: A list of sibling objects
        """
        model = type(self)
        siblings = None
        if self.parent:
            siblings = model.objects.filter(parent=self.parent).exclude(pk=self.pk)
        return siblings

    def get_siblings_ids(self):
        return self.get_siblings().values_list('id', flat=True)

    def get_all_children_flat(self):
        """
        Reduce the dictionary returned by 'get_all_children' to a flat list
        :returns: Flattened list of child objects
        """
        all_children = self.get_all_children()
        return [x for v in all_children.values() for x in v]

    def get_all_children_ids_flat(self):
        """
        Get the sorted ids of all children
        :returns: Flattened list of sorted child ids
        """
        all_children = self.get_all_children_flat()
        return sorted([child.pk for child in all_children])

    def get_siblings_children(self):
        """
        Get all decsendents of an object's siblings
        :returns: A list of all child objects of the current object's siblings
        """
        siblings = self.get_siblings()
        siblings_children = []
        for sibling in siblings:
            siblings_children.extend(sibling.get_all_children_flat())
        return siblings_children

    @property
    def has_children(self):
        return type(self).objects.filter(parent=self).exists()

    class Meta:
        abstract = True

