# -*- coding: utf-8 -*-
from django.core.cache import caches

from question.models import Questions


def count(request):
    result = {}

    cache = caches['default']

    questions_count = cache.get('questions_count')

    if questions_count is None:
        questions_count = Questions.objects.filter(is_deleted=False).count()
        cache.set('questions_count', questions_count, 300)

    result.update(questions_count=questions_count)

    return result
