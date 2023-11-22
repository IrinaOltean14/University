#include <QApplication>
//#include <QSpinBox>
//#include <QSlider>
//#include <QHBoxLayout>

#include "UI.h"
#include "Repository.h"
#include "InterestedCSV.h"
#include "InterestedHTML.h"
#include "Exceptions.h"
#include "Domain.h"
#include "GUI.h"
#include "FakeRepo.h"
#include <fstream>
void test_fake() {
    FakeRepo* repo = new FakeRepo(false);
    FakeRepo* repo1 = new FakeRepo(true);
    InterestedList* interested = new InterestedList();
    Service service{ repo , interested };
    Service service1{ repo1, interested };


    try {
        assert(service.GetIndexOfEvent("Title") == 0);
    }
    catch (exception& e) {
        assert(true);
    }

    
}

int main(int argc, char** argv) {
    std::string command;
    QApplication application(argc, argv);

    while (true) {
            InterestedList* interested = new InterestedList();
            Repository repository{ "Events.txt" };
            Service service(&repository, interested);

            test_fake();
            GUI gui(service);
            gui.show();

            return application.exec();
   
    }
    /*InterestedList* interested = new InterestedList();
    Repository repository{ "Events.txt" };
    Service service(repository, interested);


    GUI gui(service);
    gui.show();

    return QApplication::exec();*/
}