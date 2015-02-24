#!/usr/bin/env python

GENERATION_TIME = [9, 10, 21, 20, 7, 11, 4, 15, 7, 7, 14, 5, 20, 6, 29, 8,
                   11, 19, 18, 22, 29, 14, 27, 17, 6, 22, 12, 18, 18, 30]
OVERHEAD_TIME = [21, 16, 19, 26, 26, 7, 1, 8, 17, 14, 15, 25, 20, 3, 24,
                 5, 28, 9, 2, 14, 9, 25, 15, 13, 15, 9, 6, 20, 27, 22]
BUDGET = 2912


def calc_card_cost(generation_time, overhead_time, final_set_count):
    return generation_time + (overhead_time * (final_set_count-1))


def build_cards_lists(generation_list, overhead_list):
    qty_cards = len(generation_list)

    group_list = []
    for card_id in range(qty_cards):
        # for each card calc cost for each final set count (cards_count)
        for cards_count in range(1, qty_cards + 1):
            card_cost = calc_card_cost(generation_list[card_id],
                                       overhead_list[card_id],
                                       cards_count)
            group = {
                'count': cards_count,
                'card': {
                    'id': "%02d" % card_id,
                    'generation': generation_list[card_id],
                    'overhead': overhead_list[card_id],
                    'cost': card_cost,
                }
            }
            group_list.append(group)

    # sort cards_list by card time cost
    group_list.sort(key=lambda grp: grp['card']['cost'])

    groups_by_count = []
    for cards_count in range(1, qty_cards + 1):
        cards_by_count = [grp['card'] for grp in group_list
                          if grp['count'] == cards_count]
        groups_by_count.append(cards_by_count[:cards_count])

    return groups_by_count


def calc_total_cost(cards_group):
    return sum([card['cost'] for card in cards_group])


def print_cards_list(cards_list):
    print "\n".join(["card: %s (g=%s,o=%s)" %
                    (card['id'], card['generation'], card['overhead'])
                    for card in cards_list])


if __name__ == '__main__':

    # build a list of groups of cards by # of cards in the group
    cards_lists = build_cards_lists(GENERATION_TIME, OVERHEAD_TIME)

    # filter cards groups <= BUDGET
    in_budget_cards = filter(lambda grp: calc_total_cost(grp) <= BUDGET,
                             cards_lists)

    # final set: max cards group in the budget
    final_set = [] if len(in_budget_cards) == 0 \
        else max(in_budget_cards)

    # cards in final set
    # print_cards_list(final_set)

    # max # of cards is the length of final set
    print "Answer: %s" % len(final_set)  # 17
