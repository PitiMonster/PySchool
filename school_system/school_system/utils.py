# external imports
from django.shortcuts import get_object_or_404
from typing import List

# internal imports
from .models import Grade, Student, SchoolClass, Teacher, Subject, User



def get_objects_by_id(objects: List[str], request):
    try:
        result = []
        for obj in objects:
            names = obj.split('_')
            class_name = ''
            for name in names:
                if name == 'id':
                    break
                class_name += name.capitalize()

            obj_id = request.data[obj]
            result.append(get_object_or_404(eval(class_name), pk=int(obj_id)))

        return result
    except Exception as e:
        print(e)
        return [False*len(objects)]
