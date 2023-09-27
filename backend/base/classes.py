from rest_framework import generics, permissions, mixins, decorators, viewsets


class MixedPermission:
    """ Миксин permissions для action
    """
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


# базовые классы

# объединение MixedPermission с ViewSet
class MixedPermissionViewSet(MixedPermission, viewsets.ViewSet):
    pass


# объединение MixedPermission с GenericViewSet
class MixedPermissionGenericViewSet(MixedPermission, viewsets.GenericViewSet):
    pass


# объединение MixedPermission с GenericViewSet и mixins
class CreateUpdateDestroy(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            MixedPermission,
                            viewsets.GenericViewSet):
    """
    """
    pass


class CreateRetrieveUpdateDestroy(mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    MixedPermission,
                                    viewsets.GenericViewSet):
    """
    """
    pass