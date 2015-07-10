#include <fstream>
#include <vector>
#include <algorithm>

int main(int argc, char *argv[])
{
  const char * inputfile = argv[1];
  const char * outputfile = argv[2];
  std::ifstream in(inputfile, std::ios::binary);
  std::vector<char> v( (std::istreambuf_iterator<char>(in)),
      std::istreambuf_iterator<char>() );
  std::ofstream out(outputfile);
  std::copy(v.rbegin(), v.rend(), std::ostreambuf_iterator<char>(out));
  return 0;
}
