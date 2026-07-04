Users can register and update their profiles
A user's profile should contain at least their name, phone number and password
Users can participate in expenses with other users
Users can participate in groups.
To add an expense, a user must specify either the group, or the other us
u1 is asking to see the groups that they're a member of
ers involved in the expense, along with who paid what and who owes what. Th
ey must also specify a description for the expense.
A user can see their total owed amount
A user can see a history of the expenses they're involved in
A user can see a history of the expenses made in a group that they're participating in
Users shouldn't be able to query about groups they are not a member of -> RBAC (Role Based Access Control)

Only the user who has created a group can add/remove members to the group
Users can request a settle-up. The application should show a list of transactions, which when executed will ensure that the user no longer owes or recieves money from any other user. Note that this need not settle-up any other users.
Settle up option within a group so that all the members will be shown how much they owe/receive at once for all the users!.
When settling a group, we should try to minimize the number of transactions that the group members make to settle up.


Example inputs:

- u1 is asking to see the groups that they're a member of

u1 SettleUp

- u1 is asking to see the list of transactions they should perform to settle up

u1 SettleUp g1

- u1 is asking to see the list of transactions that need to be performed by members of g1 to completely settle up the group.

u1 Expense g1 iPay 1000 Equal Desc Wifi Bill


- u1 is adding an expense in the group g1. u1 paid 1000 Rs each user of g1 owes an equal amount (the exact amount will depend on the number of users in group g1. Say g1 has 5 users, then the amount owed by each will be 200Rs).

u1 Expense u2 u3 u4 iPay 1000 Equal Desc Last night dinner

- u1 is adding an expense with users u2, u3 and u4. u1 paid 1000 Rs each user owes an equal amount - 250Rs.

u1 Expense u2 u3 iPay 1000 Percent 20 30 50 Desc House rent

- u1 is adding an expense with users u2 and u3 u1 paid 1000 Rs u1 owes 20% (200Rs), u2 owes 30% (300Rs) and u3 owes 50% (500Rs).
