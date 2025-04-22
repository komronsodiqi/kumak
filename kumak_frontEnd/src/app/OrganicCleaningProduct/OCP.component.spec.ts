import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OCPComponent } from './OCP.component';

describe('organicCleaningProductComponent', () => {
  let component: OCPComponent;
  let fixture: ComponentFixture<OCPComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OCPComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(OCPComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
