from unittest import TestCase,main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.sii = Hero('zensii', 1, 10, 1)
        self.enemy = Hero('The Bad Guy', 1, 1, 1)

    def test_init(self):
        self.assertEqual('zensii', self.sii.username)
        self.assertEqual(1, self.sii.level)
        self.assertEqual(10, self.sii.health)
        self.assertEqual(1, self.sii.damage)

    def test_battle_win(self):
        self.assertEqual("You win", self.sii.battle(self.enemy))
        self.assertEqual(0, self.enemy.health)
        self.assertEqual(2, self.sii.level)
        self.assertEqual(14, self.sii.health)
        self.assertEqual(6, self.sii.damage)

    def test_battle_draw(self):
        self.sii.health = 1
        self.assertEqual("Draw", self.sii.battle(self.enemy))
        self.assertEqual(0, self.enemy.health)
        self.assertEqual(0, self.sii.health)

    def test_battle_lose(self):
        self.enemy.health = 10
        self.enemy.damage = 10
        self.assertEqual("You lose", self.sii.battle(self.enemy))
        self.assertEqual(14, self.enemy.health)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(15, self.enemy.damage)
        self.assertEqual(0, self.sii.health)

    def test_battle_exception_self_fight(self):
        with self.assertRaises(Exception) as ex:
            self.sii.battle(self.sii)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_exception_self_health_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.sii.health = -10
            self.sii.battle(self.enemy)
        self.assertEqual(f"Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_exception_enemy_health_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.enemy.health = 0
            self.sii.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))


    def test___str__(self):
        self.assertEqual(f"Hero {self.sii.username}: {self.sii.level} lvl\nHealth: {self.sii.health}\n"
                         f"Damage: {self.sii.damage}\n", self.sii.__str__())


if __name__ == '__main__':
    main()