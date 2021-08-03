from django.test import TestCase
from loguru import logger

from lw_main.models import User, Project, Node, Edge, Links
from loguru import logger

class UserTestCase(TestCase):
    def setUp(self):
        # Animal.objects.create(name="lion", sound="roar")
        # Animal.objects.create(name="cat", sound="meow")
        User.objects.create_user("TeaDove", password="best password ever")
        User.objects.create_user("TeaSparrow", password="best password ever")
        User.objects.create_user("MeeKey", password="best password ever")
        User.objects.create_user("Антон", password="best password ever")
        User.objects.create_user("Man", password="best password ever")

    def test_username(self):
        test_user = User.objects.get(username='TeaDove')
        test_user._log()
        self.assertEqual(test_user.username, 'TeaDove')
        self.assertTrue(test_user.check_password('best password ever'))


class ProjectTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create_user("TeaDove", password="best password ever")
        project = Project.objects.create(title="Лучшая доска по изучению Питона", user=test_user)
        self.project__ = project

    def test_relationship(self):
        test_user = User.objects.get(username='TeaDove')
        self.project__._log()
        self.assertEqual(self.project__.user.id, test_user.id)


class EverythingTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create_user("TeaDove", password="best password ever")
        project = Project.objects.create(title="Лучшая доска по изучению Питона", user=test_user)
        project2 = Project.objects.create(title="Лучшая доска по изучению Го", user=test_user)
        self.nodes = [Node.objects.create(title="Питон", project=project),
                      Node.objects.create(title="SQL", project=project),
                      Node.objects.create(title="ORM", project=project),
                      Node.objects.create(title="Типы данных", project=project),
                      Node.objects.create(title="Память", project=project),
                      Node.objects.create(title="Алгоритмы", project=project)]

        self.edges = [Edge.objects.create(node_1=self.nodes[0], node_2=self.nodes[1]),
                      Edge.objects.create(node_1=self.nodes[2], node_2=self.nodes[1], direction='forward'),
                      Edge.objects.create(node_1=self.nodes[0], node_2=self.nodes[5]),
                      Edge.objects.create(node_1=self.nodes[3], node_2=self.nodes[2], direction='backward'),
                      Edge.objects.create(node_1=self.nodes[4], node_2=self.nodes[1], direction='backward'),
                      Edge.objects.create(node_1=self.nodes[5], node_2=self.nodes[0], direction='backward')]

    def test_everything(self):
        test_user = User.objects.get(username='TeaDove')
        [project._log() for project in test_user.projects.all()]
        logger.info('Edges')
        for edge in self.edges:
            to_return = '{}: {}, {}'.format(edge.id, edge.node_1.id, edge.node_2.id)
            logger.info(to_return)

        logger.info('Nodes')
        for node in self.nodes:
            edge_ids = [edge.id for edge in node.get_all_edges()]
            to_return = '{}: {}'.format(node.id, edge_ids)
            logger.info(to_return)

