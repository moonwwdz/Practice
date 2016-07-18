package stack

//栈的结构
type Stack struct {
	TopStack *MemSpace
	//	BotStack *MemSpace
	Size int
}

//栈内元素的结构
type MemSpace struct {
	Prev    *MemSpace
	Element string
	Next    *MemSpace
}

//创建一个空栈
func (s *Stack) CreatStack() {
	return new(Stack{})
}

//返回栈顶的元素
func (s *Stack) Top(this *Stack) *MemSpace {
	return this.TopStack

}

//取出顶部元素
func (s *Stack) Pop(this *Stack) string {
	var r *MemSpace
	if this.TopStack.Prev != nil {
		r, this.TopStack.Prev.Next = this.TopStack, nil
		this.Size--
	}
	return r.Element
}

//顶部压入元素
func (s *Stack) Push(this *Stack, e string) bool {
	if len(e) <= 0 {
		return false
	}
	m := new(MemSpace)
	this.TopStack.Next = m
	*m = MemSpace{m, e, nil}
	this.Size++
	return true
}

//清空栈
func (s *Stack) Empty(this *Stack) {
	this.TopStack.Prev = nil
}
