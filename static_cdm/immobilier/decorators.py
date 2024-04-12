import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def group_required(group, login_url=None, raise_exception=False):
    def check_perms(Auteruser):
        if isinstance(group, six.string_types):
            groups=(group, )
        else:
            groups =group
            # First check if the user has the permission (even anon users)    
            #Vérifiez d'abord si l'utilisateur a l'autorisation (même les utilisateurs anonymes)
        if Auteruser.groups.filter(name__in=group).exists():
            return True
            # In case the 403 handler should be called raise the exception
            #Dans le cas où le gestionnaire 403 devrait être appelé, déclenchez l'exception
        if raise_exception:
            raise PermissionDenied
            # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, login_url="login")    
