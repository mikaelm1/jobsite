import logging
from django.shortcuts import redirect
from django.contrib import messages

logger = logging.getLogger(__name__)


def deny_acces(request):
    messages.error(request, 'Access denied')
    return redirect('/')


def employer_access(user):
    if hasattr(user, 'employer'):
        return user.employer is not None
    logger.warning('User {} trying to access employer view.'.format(user))
    return False


def seeker_access(user):
    if hasattr(user, 'seeker'):
        return user.seeker is not None
    logger.warning('User {} trying to access seeker view.'.format(user))
    return False
