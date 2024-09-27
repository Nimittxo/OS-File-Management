#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <filename> <content>" << std::endl;
        return 1;
    }

    const char* file_name = argv[1];
    const char* content = argv[2];

    std::ofstream createfile(file_name);
    if (createfile.is_open()) {
        createfile << content;
        createfile.close();
        std::cout << "File '" << file_name << "' created successfully!" << std::endl;
    } else {
        std::cerr << "Error creating file '" << file_name << "'!" << std::endl;
        return 1;
    }

    return 0;
}
