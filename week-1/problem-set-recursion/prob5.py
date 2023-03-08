def transfer_books(n, source, target, helper):
    """
    This function recursively transfers n books from the source basket to the target basket, 
    with the help of the helper basket. The books must be transferred in the same order 
    and according to the given rules.
    
    :param n: number of books to transfer
    :param source: source basket
    :param target: target basket
    :param helper: helper basket
    """
    if n == 1:
        if (source[-1] == 'Physics' and target[-1] == 'Chemistry'):
            raise ValueError("Invalid move: Physics book can't be on top of Chemistry book")
        if ((source[-1] == 'Physics' or source[-1] == 'Chemistry') and target[-1] == 'Math'):
            raise ValueError("Invalid move: Physics and Chemistry books can't be on top of Maths book")
        print(f"Move {source[-1]} from {source} to {target}")
        target.append(source.pop())
        return
    transfer_books(n-1, source, helper, target)
    print(f"Move {source[-1]} from {source} to {target}")
    target.append(source.pop())
    transfer_books(n-1, helper, target, source)

# Initial baskets
source = ['Physics', 'Chemistry', 'Maths']
target = []
helper = []

# Transfer books from source to target
transfer_books(len(source), source, target, helper)

print(source)
print(target)
print()

# Cleaner code. Mimic Tower of Hanoi
def move_books(num_books, source, target, helper):
    if num_books == 1:
        print(f"Move book {books[num_books-1]} from {source} to {target}")
    else:
        move_books(num_books-1, source, helper, target)
        print(f"Move book {books[num_books-1]} from {source} to {target}")
        move_books(num_books-1, helper, target, source)

books = ["Maths", "Chemistry", "Physics"]
num_books = 3
source = "basket 1"
target = "basket 2"
helper = "basket 3"
move_books(num_books, source, target, helper)
