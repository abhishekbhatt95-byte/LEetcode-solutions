class Solution {
    public ListNode addTwoNumbers(ListNode L1, ListNode L2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;

        while (L1 != null || L2 != null || carry != 0) {
            int sum = carry;

            if (L1 != null) {
                sum += L1.val;
                L1 = L1.next;
            }
            if (L2 != null) {
                sum += L2.val;
                L2 = L2.next;
            }

            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;
        }

        return dummy.next;
    }
}