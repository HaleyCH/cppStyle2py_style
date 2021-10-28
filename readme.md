# cppStyle2py_style

## Usage:
1. You can convert a cpp style code to py style by using command as follow
```
python cppStyle2py_style Your/File/Address.cpp
```
2. It will create the output file  `Your/File/Address_trans.cpp`.

# Have fun!

### Notice! It may break the struct of your programme, so please use it just for fun!

# Sample:
## origin:
```struct ListNode{
    int val;
    ListNode* next = nullptr;
    explicit ListNode(int v):val(v){};
};

class List{
public:
    ListNode *head= nullptr;
    List(){create_list();};
    ~List()= default;
    int  find_first(int v) const;
    List *add(int v);
    List *insert_after(int pos,int v);
    ListNode *pop() const;
    List *clear();
private:
    void create_list();
};

```

## after convert:
```List_node                                                      {
     int val                                                           ;
     List_node* next = nullptr                                         ;
     explicit List_node(int v):val(v){}                                ;
 }                                                                     ;
  class List                                                            {
 public                                                                :
     List_node *head= nullptr                                          ;
     List(){create_list();}                                            ;
     ~_list()= default                                                 ;
     int  find_first(int v) const                                      ;
     List *add(int v)                                                  ;
     List *insert_after(int pos,int v)                                 ;
     List_node *pop() const                                            ;
     List *clear()                                                     ;
 private                                                               :
     void create_list()                                                ;
 }                                                                     ;```