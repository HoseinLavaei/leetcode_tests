import importlib
import pkgutil

def run_all_tests():
    user_packages = ['hosein', 'amir']
    
    for user_name in user_packages:
        try:
            user_package = importlib.import_module(user_name)
        except ImportError:
            print(f"Could not import package: {user_name}")
            continue

        print(f"Running tests for {user_name}...")

        submodules = sorted(pkgutil.iter_modules(user_package.__path__), key=lambda x: x.name)
        
        for loader, module_name, is_pkg in submodules:
            if not(is_pkg and module_name.startswith("LC")):
                continue
            full_module_name = f"{user_name}.{module_name}"
            try:
                module = importlib.import_module(full_module_name)
                for attr_name in sorted(dir(module)):
                    if attr_name.startswith("test_"):
                        test_func = getattr(module, attr_name)
                        if callable(test_func):
                            print(f"  Calling {full_module_name}.{attr_name}()")
                            test_func()
            except Exception as e:
                print(f"  Error importing/running {full_module_name}: {e}")


def main():
    run_all_tests()

if __name__ == "__main__":
    main()
