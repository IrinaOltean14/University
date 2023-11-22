#include <stdio.h>
#include <stdlib.h>

#include "Repository.h"
#include "Service.h"
#include "ui.h"
#include "undo.h"

int main()
{
	Repository* repo = createRepo();
	Undo* undo = create_undo();
	Undo* redo = create_undo();
	Service* service = createService(repo, undo, redo);
	Ui* ui = createUi(service);
	add_entries(ui);
	test(ui);
	printMenu(ui);

	
	return 0;
}


