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
func (s *Stack) CreatStack() *Stack {
	return new(Stack)
}

//返回栈顶的元素
func (s *Stack) TopMem(this *Stack) *MemSpace {
	return this.TopStack.Element

}

//取出顶部元素
func (s *Stack) PopMem(this *Stack) string {
	var r *MemSpace = this.TopStack
	if this.TopStack.Prev != nil {
		this.TopStack, this.TopStack.Next = this.TopStack.Prev, nil
		this.Size--
	}
	return r.Element
}

//顶部压入元素
func (s *Stack) PushMem(this *Stack, e string) bool {
	if len(e) <= 0 {
		return false
	}
	m := &MemSpace{Prev: nil, Next: nil, Element: e}
	if this.TopStack != nil {
		m.Prev, this.TopStack.Next = this.TopStack, m
	}
	this.TopStack = m
	this.Size++
	return true
}

//清空栈
func (s *Stack) EmptyMem(this *Stack) {
	this.TopStack.Prev = nil
}
