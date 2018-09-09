
class Dlog:
        
    def resp(request):
        print("========================================")
        print("           R  E  Q  U  E  S  T          ")
        print("========================================")
        for key, val in request.POST.items():
            print(str(key) + " : " + str(val))