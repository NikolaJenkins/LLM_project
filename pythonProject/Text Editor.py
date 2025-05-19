from typing import Optional


class Node:
    val: str
    next: Optional["Node"]
    prev: Optional["Node"]


class TextEditor(object):

    def __init__(self):
        self.left_of_cursor: Optional[Node] = None
        self.right_of_cursor: Optional[Node] = None

    def addText(self, text: str) -> None:
        for char in text:
            next = Node()
            next.val = char
            next.prev = self.left_of_cursor
            self.left_of_cursor = next
        return None

    def deleteText(self, k: int) -> int:
        deleted_characters = 0
        while self.left_of_cursor is not None and deleted_characters < k:
            deleted_characters += 1
            self.left_of_cursor = self.left_of_cursor.prev
            self.left_of_cursor.next = None
        return deleted_characters

    def cursorLeft(self, k: int) -> str:
        moved_characters = 0
        while self.left_of_cursor is not None and moved_characters < k:
            moved_characters += 1
            prev_right = self.right_of_cursor
            self.right_of_cursor = self.left_of_cursor
            self.right_of_cursor.prev = None
            self.right_of_cursor.next = prev_right
            self.left_of_cursor = self.left_of_cursor.prev
            self.left_of_cursor.next = None
        return self.charsToLeft()

    def cursorRight(self, k: int) -> str:
        moved_characters = 0
        while self.right_of_cursor is not None and moved_characters < k:
            moved_characters += 1
            prev_left = self.left_of_cursor
            self.left_of_cursor = self.right_of_cursor
            self.left_of_cursor.next = None
            self.left_of_cursor.prev = prev_left
            self.right_of_cursor = self.right_of_cursor.next
            self.right_of_cursor.prev = None
        return self.charsToLeft()

    def charsToLeft(self) -> str:
        prevPointer = self.left_of_cursor
        reversedList = list()
        accumChar = 0
        while prevPointer is not None and accumChar < 10:
            accumChar += 1
            reversedList.append(prevPointer.val)
            prevPointer = prevPointer.prev
        return "".join(reversed(reversedList))


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
textEditor = TextEditor() # The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode") # The current text is "leetcode|".
assert (textEditor.deleteText(4)) == 4 # return 4
textEditor.addText("practice") # The current text is "leetpractice|".
assert textEditor.cursorRight(3) == "etpractice" # return "etpractice"
#                            // The current text is "leetpractice|".
#                            // The cursor cannot be moved beyond the actual text and thus did not move.
#                            // "etpractice" is the last 10 characters to the left of the cursor.
# textEditor.cursorLeft(8); // return "leet"
#                           // The current text is "leet|practice".
#                           // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
# textEditor.deleteText(10); // return 4
#                            // The current text is "|practice".
#                            // Only 4 characters were deleted.
# textEditor.cursorLeft(2); // return ""
#                           // The current text is "|practice".
#                           // The cursor cannot be moved beyond the actual text and thus did not move.
#                           // "" is the last min(10, 0) = 0 characters to the left of the cursor.
# textEditor.cursorRight(6); // return "practi"
#                            // The current text is "practi|ce".
#                            // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.