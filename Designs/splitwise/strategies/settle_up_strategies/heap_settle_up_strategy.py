from typing import List, Dict
from heapq import heapify, heappop, heappush

from .settle_up_strategy import SettleUpStrategy
from models import ExpenseOwingUser, ExpensePayingUser, Transaction

class HeapSettleUpStrategy(SettleUpStrategy):

    def get_transactions(self, paying_expenses: List[ExpensePayingUser], owing_expenses: List[ExpenseOwingUser]) -> List[Transaction]:
        transactions : List[Transaction] = []
        expense_map: Dict[ExpensePayingUser|ExpenseOwingUser, int] = {}
        for payer in paying_expenses:
            if payer not in expense_map:
                expense_map[payer] = 0
            expense_map[payer] += payer.amount

        for ower in owing_expenses:
            if ower not in expense_map:
                expense_map[ower] = 0
            expense_map[ower] -= ower.amount

        # expense_map will have a final value of who is owed who much and who has to pay how much.

        paying_queue: List[List[int | ExpensePayingUser]] = heapify([])
        owing_queue: List[List[int | ExpenseOwingUser]] = heapify([])

        for exp_user in expense_map:
            if expense_map[exp_user] < 0:
                # we have to store such that the lowest comes first
                heappush(paying_queue, [expense_map[exp_user], exp_user])
            elif expense_map[exp_user] > 0:
                # we have to store such that the highest comes first
                heappush(owing_queue, [-expense_map[exp_user], exp_user])
            # ignore 0 as they are already settled

        while paying_queue and owing_queue:
            paying, owing = heappop(paying_queue), heappop(owing_queue)

            if abs(paying[0]) < abs(owing[0]):
                transactions.append(Transaction(owing[1].user, paying[1].user, abs(paying[0])))
                heappush(owing_queue, -(abs(owing[0]) - abs(paying[0])))
            elif abs(paying[0]) > abs(owing[0]):
                heappush(paying_queue, -(abs(paying[0]) - abs(owing[0])))
                transactions.append(Transaction(owing[1].user, paying[1].user, abs(owing[0])))

        return transactions