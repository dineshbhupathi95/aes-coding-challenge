# The Setup

1. Create a virtual environment, python 3.6+.
2. Install dependencies mentioned in requirements.txt file
3. To check if its working run :
 	=> python manage.py runserver
4. To apply in-built migrations:
	=> python manage.py migrate
5. To populate masters, run:
	=> python manage.py populate_masters
6. Your code goes in the `transaction` directory



# The question

**Objective:**

To create APIs for a transaction.

**Requirements:**

Tech Stack - Django, Python 3.6+

For creation of APIs - Can use Django Rest Framework.

**PART A: Models**

1.  **Transaction**
       
    1.  Fields
        
        1.  Unique Id - auto_generated primary field
            
        2.  Company - linked to CompanyLedgerMaster - display CompanyLedgerMaster name in response
            
        3.  Branch - linked to BranchMaster - display BranchMaster short_name in response
            
        4.  Department - linked to DepartmentMaster- display DepartmentMaster name in response
            
        5.  Transaction Number - unique for each transaction
            
            1.  Format - TRN/{COUNT}/{YEAR}
                
            2.  Count here should reset to 1 for every year.
                
        6.  Transaction Status - Choice Field. Could be PENDING/COMPLETED/CLOSE
            
        7.  Remarks - Char field. Is optional
            
2.  **Transaction Line Item Details**
    
    1.  Each transaction can have multiple item details
        
    2.  Fields
        
        1.  Unique Id - auto_generated primary field
            
        2.  Article - linked to ArticleMaster- display ArticleMaster name in response
            
        3.  Colour - linked to ColorMaster - display ColorMaster name in response
            
        4.  Required on date - A date-time field
            
        5.  Quantity - Decimal Field.
            
        6.  Rate per unit - Integer Field
            
        7.  Unit - Choice Field.Can be KG/METRE
            
3.  **Inventory Item**
    
    1.  Each above line item consists of multiple inventory items.
        
    2.  Fields
        
        1.  Unique Id - auto_generated primary field
            
        2.  Article - linked to ArticleMaster- display ArticleMaster name in response
            
        3.  Colour - linked to ColorMaster - display ColorMaster name in response
            
        4.  Company -linked to CompanyLedgerMaster - display CompanyLedgerMaster Name in response
            
        5.  Gross Quantity - Decimal field.
            
        6.  Net Quantity - Decimal field.
            
        7.  Unit - Choice Field.Can be KG/METRE
            

**PART B: APIs to create**

1.  Add a transaction document with its line items.
    
2.  Add line items once a transaction is created.
    
3.  Add multiple inventory items to line items.
    
4.  Delete a transaction, cant be deleted if inventory is created.
    
5.  View a transaction with all its line items and their inventory items.
    

**PART C: Validations (Optional)**

1.  Two line items in a transaction cant have same combination of article and colour.
    
2.  Colour chosen should have a link with chosen article.
    
3.  All response should be in a format:
    

`{ "data": {}, "message": "", "status": <SOME HTTP STATUS CODE> }`

Here,

If the response is successful, it should be returned in the "data" field ;

"message" tells us error in case of any.

"status" is an http response status code.

