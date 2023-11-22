#include "InterestedHTML.h"
#include <fstream>

HTMLInterested::HTMLInterested() = default;

HTMLInterested::~HTMLInterested() = default;

//void HTMLInterested::saveToFile() {
//    ofstream filestream("interestedlist.html");
//
//    filestream << "<!DOCTYPE html>" << "\n";
//    filestream << "<html>" << "\n";
//
//    filestream << "<head>" << "\n";
//    filestream << "<title>Interested List</title>" << "\n";
//    filestream << "</head>" << "\n";
//
//    filestream << "<body>" << "\n";
//
//    filestream << "<table border=\"1\">" << "\n";
//
//    filestream << "<tr>" << "\n";
//    filestream << "<td>Name</td>" << "\n";
//    filestream << "<td>Description</td>" << "\n";
//    filestream << "<td>Year</td>" << "\n";
//    filestream << "<td>Month</td>" << "\n";
//    filestream << "<td>Day</td>" << "\n";
//    filestream << "<td>Hour</td>" << "\n";
//    filestream << "<td>Minute</td>" << "\n";
//    filestream << "<td>Number of people</td>" << "\n";
//    filestream << "<td>Link</td>" << "\n";
//    filestream << "</tr>" << "\n";
//
//    for (const auto& event : this->events)
//    {
//        filestream << "<tr>" << "\n";
//
//        filestream << "<td>" << event.GetTitle() << "</td>" << "\n";
//        filestream << "<td>" << event.GetDescription() << "</td>" << "\n";
//        filestream << "<td>" << event.GetDate().year << "</td>" << "\n";
//        filestream << "<td>" << event.GetDate().month << "</td>" << "\n";
//        filestream << "<td>" << event.GetDate().day << "</td>" << "\n";
//        filestream << "<td>" << event.GetDate().hour << "</td>" << "\n";
//        filestream << "<td>" << event.GetDate().minute << "</td>" << "\n";
//        filestream << "<td>" << event.GetPeople() << "</td>" << "\n";
//        filestream << "<td><a href =" << event.GetLink() << ">Link</a></td>";
//
//        filestream << "</tr>" << "\n";
//    }
//
//    filestream << "</table>" << "\n";
//
//    filestream << "</body>" << "\n";
//
//    filestream << "</html>" << "\n";
//    filestream.close();
//}
//
//void HTMLInterested::openInApp() {
//    system(R"(explorer.exe C:\Users\Cristina\Documents\GitHub\a7-IrinaOltean14-1\A7\A7\interestedlist.html)");
//}